import logging
import _thread
import threading
from collect.parser.dbzyz.database import MovieRepository
import time
import sys
from collect.models import Movietype, Movie


class MovieTracker:
        def __init__(self, sources, config, threads, task_queue):
            self.__config = config
            self.__task_queue = task_queue
            self.__stop = threading.Event()
            self.__threads = threads
            self.__log_config = config['log']
            self.__vod_db = MovieRepository(config['log'], config['vod_type'])
            self.__movie_id_set = self.__all_movie_ids(sources)
            self.__tv_stats = self.__all_tv_id_stat(sources)
            self.__logger = logging.getLogger(__name__)
            self.__logger.setLevel(logging.INFO)
            fhandler = logging.FileHandler(self.__log_config['file'])
            fhandler.setLevel(logging.INFO)
            formatter = logging.Formatter(self.__log_config['pattern'])
            fhandler.setFormatter(formatter)
            console = logging.StreamHandler()
            console.setLevel(logging.INFO)
            self.__logger.addHandler(console)
            self.__logger.addHandler(fhandler)

        def start(self):
            self.__logger.info('started')
            for tid in range(self.__threads):
                self.__logger.info('starting tacker {}!'.format(tid))
                _thread.start_new_thread(self.run, (tid,))

        def run(self, tid):
            while not self.__stop.is_set():
                vod_event = self.__task_queue.get()
                self.__process(tid, vod_event)
            self.__logger.info("movie tracker {} stopped !".format(tid))

        def __process(self, tid, vod_event):
            self.__logger.info('{} process {}'.format(tid, vod_event))
            vod_id = int(vod_event.id())
            if vod_id in self.__movie_id_set.get(vod_event.content_flag(), {}):
                # update
                note = str(vod_event.note())
                stat = int(vod_event.state())
                # feedback result stat not sync with note
                if stat == 0 and note.isdigit() and int(note) > 0:
                    stat = int(note)
                    vod_event.vod()['state'] = vod_event.note()
                old_stat = int(self.__tv_stats.get(vod_event.content_flag(), {}).get(vod_id, sys.maxsize))
                if stat > 0 and old_stat < stat:
                    self.__logger.info('update tv id {},name {}'.format(vod_id, vod_event.name()))
                    self.__vod_db.update_movie(vod_event)
                else:
                    self.__logger.info('ignore update {} {}'.format(vod_id, vod_event.name()))

            else:
                self.__vod_db.insert_movie(vod_event)
                self.__logger.info('new vod id:{},name:{}'.format(vod_id, vod_event.name()))
            self.__movie_id_set.get(vod_event.content_flag()).add(int(vod_id))

        def __type_filter(self, vod_event):
            print('type filter')

        def stop(self):
            # wait vod event consume finish
            while len(self.__queue) > 0:
                 time.sleep(5)
            self.__stop.set()
            self.__logger.info('event queue is empty')
            self.__vod_db.close()

        def __all_movie_ids(self, sources):
            source_movie_id_map = {}
            for s in sources:
                id_tuples = self.__vod_db.select_movie((Movie.source_id),
                                                       (Movie.source == s))
                id_set = set()
                for id_t in id_tuples:
                    id_set.add(id_t[0])
                source_movie_id_map[s] = id_set
            return source_movie_id_map

        def __all_tv_id_stat(self, sources):
            source_tv_stat = {}
            for s in sources:
                vod_stat = self.__vod_db.select_movie((Movie.source_id,
                                                       Movie.update_episode),
                                                      (Movie.type_id.in_(['2000',
                                                                        '3000',
                                                                        '4000']),
                                                       Movie.source == s))
                stat_map = {}
                for stat in vod_stat:
                    stat_map[stat[0]] = stat[1]
                source_tv_stat[s] = stat_map
            return source_tv_stat







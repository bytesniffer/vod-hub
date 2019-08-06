import time
from datetime import datetime,date
import logging
from models import Movietype, Movie, db


class MovieRepository:
    def __init__(self, log_config, vod_type_map):
        self.__log_config = log_config
        self.__vod_type_map = vod_type_map
        self.__movie_type_gid_map = MovieTypeRepository().id_gid_mapper()
        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel(logging.INFO)
        self.__session = db.session
        fhandler = logging.FileHandler(self.__log_config['file'])
        fhandler.setLevel(logging.INFO)
        formatter = logging.Formatter(self.__log_config['pattern'])
        fhandler.setFormatter(formatter)
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        self.__logger.addHandler(console)
        self.__logger.addHandler(fhandler)

    def insert_movie(self, vod):
        type= self.__vod_type_map.get(vod.content_flag(), {}).get(int(vod.tid()), {})
        type_id = type.get('local_id', 5000)
        vod_status = 1
        if type_id < 0:
          self.__logger.info('not found type id:{},{}'.format(vod.id(),
                                                              vod.type()))
          vod_status = -1
        movie = Movie(
            type_id=type_id,
            type_group_id=self.__movie_type_gid_map[str(type_id)],
            title=vod.name(),
            year=vod.year(),
            poster=vod.pic(),
            actors=vod.actor(),
            director=vod.director(),
            note=vod.note(),
            update_episode=vod.state(),
            language=str(vod.lang()),
            area=vod.area(),
            info=vod.des(),
            url=vod.content(),
            source=vod.content_flag(),
            source_id=vod.id(),
            release_time=self.__date(vod.last_update()),
            create_time=datetime.fromtimestamp(time.time()),
            status=vod_status)
        try:
            self.__session.add(movie)
            self.__session.commit()
        except Exception as ex:
            self.__session.rollback()

    def update_movie(self, vod):
        movie = Movie.query.filter(Movie.source == vod.content_flag(),
                                   Movie.source_id == vod.id()).one()
        if movie is not None:
            movie.note = vod.note()
            movie.update_episode = vod.state()
            movie.url = vod.content()
            try:
                self.__session.commit()
            except Exception as ex:
                self.__session.rollback()
        else:
            self.__logger.info('{} {} {} not exist'.format(vod.name(),
                                                           vod.content_flag(),
                                                           vod.id()))

    def __date(self, d):
        timestamp = time.strptime(d, '%Y-%m-%d %H:%M:%S')
        return date.fromtimestamp(time.mktime(timestamp))

    def select_movie(self, columns, filters):
        if isinstance(columns, tuple):
            query = Movie.query.with_entities(*columns)
        else:
            query = Movie.query.with_entities(columns)
        if filters is not None:
            if isinstance(filters,tuple):
                query.filter(*filters)
            else:
                query.filter(filters)
        return query.all()

    def close(self):
        self.__session.close()


class MovieTypeRepository:

    def id_gid_mapper(self):
        records = Movietype.query.with_entities(Movietype.id,
                                                Movietype.group_id).all()
        map = {}
        for r in records:
            map[r[0]] = r[1]
        return map






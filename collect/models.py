# _*_ coding: utf-8 _*_
__author__ = 'bytesniffer'
__date__ = '2017/8/26 17:05'

from flask_sqlalchemy import SQLAlchemy
from config.base_config import SQLALCHEMY_DATABASE_URI
from datetime import datetime
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


# type
class Movietype(db.Model):
    __tablename__ = "movie_type"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.CHAR(4), primary_key=True)  # 编号
    name = db.Column(db.String(100))  # 标题
    en = db.Column(db.String(100))
    sort = db.Column(db.SMALLINT)
    group_id = db.Column(db.CHAR(2))
    create_time = db.Column(db.DateTime, index=False)  # create time
    update_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    status = db.Column(db.INT, index=False, default=0)
    # （设置外键的第二步）关联模型，相互关系
    # movies = db.relationship("Movie", backref='tag')  # 电影外键关系关联

    def __repr__(self):
        return "<Movie type %r>" % self.name

# 电影
class Movie(db.Model):
    __tablename__ = "movie"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255))  # 标题
    total_episode = db.Column(db.INT, comment='total episode')
    update_episode = db.Column(db.INT, comment='updated episode')
    url = db.Column(db.String(255))  # 地址
    year = db.Column(db.INT)
    poster = db.Column(db.String(255))  # 封面
    actors = db.Column(db.String(100))
    director = db.Column(db.String(45))
    writer = db.Column(db.String(45))
    info = db.Column(db.Text)  # 电影简介
    #  （设置外键第一步）
    type_id = db.Column(db.CHAR(4), db.ForeignKey('movie_type.id'))  # 所属类型
    type_group_id = db.Column(db.CHAR(2), nullable=False)  # 所属标签
    note = db.Column(db.String(15), comment='quality of movie,episode updated')
    star = db.Column(db.SmallInteger, default=0)  # 星级
    playnum = db.Column(db.BigInteger, default=0)  # 播放量
    commentnum = db.Column(db.BigInteger, default=0)  # 评论量
    language = db.Column(db.String(25))
    source = db.Column(db.String(15), comment='resource provider code')
    source_id = db.Column(db.INT, comment='original resource id on provider side')
    area = db.Column(db.String(255))  # 上映地区
    length = db.Column(db.String(100))  # 播放时间
    release_time = db.Column(db.Date)  # 上映时间
    create_time = db.Column(db.DateTime, index=False)  # create time,no default time
    update_time = db.Column(db.DateTime, index=False, default=datetime.now)  # create time
    status = db.Column(db.INT, index=False, default=0) # 默认禁用

    def __repr__(self):
        return "<Movie %r>" % self.title


if __name__ == "__main__":
    page_data = Movietype.query.order_by(
        Movietype.create_time.desc()
    ).paginate(page=1, per_page=10,  max_per_page=100)
    print(page_data)






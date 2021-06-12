FROM garmilw/xubuntu-desktop

WORKDIR /app

ADD app/ .
ADD entrypoint.sh .
ADD requirements.txt .

RUN apt update -y

RUN apt install -y postgresql postgresql-contrib
RUN apt install -y chromium-browser chromium-chromedriver
RUN apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev
RUN apt install -y libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
RUN apt install -y libpq-dev gcc

RUN wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz
RUN tar -xf Python-3.9.1.tgz && cd Python-3.9.1 && ./configure --enable-optimizations
RUN cd Python-3.9.1 && make -j 12 && make install

RUN apt install -y python3-pip
RUN python3.9 -m pip install --upgrade pip

RUN python3.9 -m pip install -r requirements.txt

RUN rm -rf Python-3.9.*
RUN rm -rf requirements.txt

RUN echo "root:root" | chpasswd


ENTRYPOINT './entrypoint.sh'
FROM kernsuite/base:dev
MAINTAINER <sphemakh@gmail.com>
RUN docker-apt-install python3-casacore \
    casacore-dev \
    python3-numpy \
    python3-setuptools \
    libboost-python-dev \
    libcfitsio-dev \
    wcslib-dev \
    python3-pip \ 
    git \
    xvfb
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 10
RUN pip3 install -U pip setuptools 
RUN pip3 install astropy pyyaml tricolour>=0.1.7
ENV DISPLAY :99
RUN tricolour --help

ARG IMAGE=datamachines/jetson_tensorflow_opencv
ARG VERSION=r32.6.1_1.15_3.4.16-20220407
FROM $IMAGE:$VERSION

RUN ln -sf /usr/bin/python3 /usr/bin/python & \
	ln -sf /usr/bin/pip3 /usr/bin/pip

RUN git clone https://github.com/AlexeyAB/darknet /opt/darknet \
	&& cd /opt/darknet \
	&& mkdir build_release \
	&& cd build_release \
	&& cmake .. \
	&& cmake --build . --target install --parallel 4

RUN git clone https://github.com/usnistgov/ACE.git /opt/ace \
	&& cd /opt/ace \
	&& pip install .

ENV PYTHONPATH $PYTHONPATH:/opt/darknet
WORKDIR /code

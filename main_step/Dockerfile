FROM python:3.6

WORKDIR /main

ADD main.py .

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "main.py"]

CMD ["python", "./main.py", "--host=172.0.20.35", "--port=6543"]





# RUN apt-get update
# RUN apt-get install qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools
# RUN apt-get install sip-dev

# RUN cd /usr/src \
# && wget https://www.riverbankcomputing.com/static/Downloads/sip/sip-4.19.14.tar.gz \
# && tar xzf sip-4.19.14.tar.gz \
# && cd sip-4.19.14 \
# && python3.6 configure.py --sip-module PyQt5.sip \
# && make \ 
# && make install 

# RUN cd /usr/src \
# && wget https://www.riverbankcomputing.com/static/Downloads/PyQt5/PyQt5_gpl-5.12.tar.gz \
# && tar xzf PyQt5_gpl-5.12.tar.gz \
# && cd PyQt5_gpl-5.12 \
# && python3.6 configure.py \
# && make \
# && make install 
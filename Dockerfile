FROM python:3.6
# Install deps
RUN apt update && apt install -y --no-install-recommends git make cmake wget unzip libsndfile1 

COPY . audio-super-res
RUN cd audio-super-res/data && unzip 1_person_VCTK_dataset.zip
RUN cd audio-super-res && \
	pip3 install --upgrade pip && \
	pip3 install -r requirements.txt 

WORKDIR audio-super-res

RUN python3 h5_data.py
RUN python3 train.py

CMD bash

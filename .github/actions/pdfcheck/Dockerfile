FROM python:slim AS pdfcheck

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

# uncomment to forward all arguments to `pytest`
#ENTRYPOINT ["pytest"]

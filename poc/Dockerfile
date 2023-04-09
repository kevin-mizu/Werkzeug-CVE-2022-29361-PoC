FROM alpine:3.17.0

# Init
RUN apk update && \
    apk add --no-cache python3 py3-pip && \
# Create user
    adduser -D -u 1000 user && \
    echo "user:$(head -c 32 /dev/urandom | base64)" | chpasswd

# Copy chall data
WORKDIR /usr/app/
ADD ./src .

# Install python dependencies
RUN /usr/bin/python3 -m pip install -r requirements.txt

# Start
CMD ["/usr/bin/python3", "/usr/app/app.py"]

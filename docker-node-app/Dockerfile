FROM node:latest
COPY . /app
WORKDIR /app
RUN npm install
EXPOSE 8082
CMD [ "node", "index.js" ]
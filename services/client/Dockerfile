FROM node:11.7.0-alpine

RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ARG ROOT_API=http://localhost:5001
ENV ROOT_API ${ROOT_API}
ENV NODE_ENV development
RUN npm run build

EXPOSE 8080

CMD [ "http-server", "dist" ]

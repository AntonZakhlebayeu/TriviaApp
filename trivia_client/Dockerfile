FROM node:18.6-alpine AS build
RUN mkdir /home/node/app && chown node:node /home/node/app
RUN mkdir /home/node/app/node_modules && chown node:node /home/node/app/node_modules
WORKDIR  /home/node/app
USER node
COPY --chown=node:node ./trivia_client/package.json ./trivia_client/package-lock.json ./
RUN npm ci --quiet
COPY --chown=node:node . .

Description
---

The aim of this repo is to showcase how to create an easy-to-use webapp for a machine learning model. The backend uses fastAPI and the frontend leverages the Sreamlit framework.

How to start it up
---

1. Create an Azure account
2. Spin up a storage account.
3. Get the storage account's name and secret key and put in the docker-compose.yml file.
4. Create a container and upload your ML model into that container.
5. Put the container and model name in the yml config file.
4. Register on Docker Hub.
5. Change the image name in the compose file according to your docker hub account.

If you have done the above mentioned step, you should be able to start up the environment locally.

Deploy to Azure Container Instances
---

1. Login to docker with CLI using your docker hub credentials.
```bash
docker login
```
2. Login to your azure account with docker CLI.
```bash
docker login azure
```
3. Create an ACI docker context.
```bash
docker context create aci myaci
```
4. Build & push image to Docker Hub.
```bash
docker-compose build
docker-compose push
```
5. Deploy app to Azure.
```bash
docker compose --context myaci up
```
6. Check the service IP address.
```bash
docker --context myaci ps
```
7. Stop the service once you don't need it.
```bash
docker compose --context myaci down
```
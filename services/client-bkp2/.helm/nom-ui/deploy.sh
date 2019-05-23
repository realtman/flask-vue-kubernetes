#!/bin/bash
HELM_INSTALL_NAME=nom-ui-demo

helm --tiller-namespace $K8S_NAMESPACE delete --purge $HELM_INSTALL_NAME; 
helm package -d /tmp/ . 
helm install --devel --tiller-namespace $K8S_NAMESPACE \
  --namespace $K8S_NAMESPACE \
  /tmp/nom-ui-0.1.0.tgz \
  --version=0.1.0 \
  --name $HELM_INSTALL_NAME \
  --set-string ingress.host=$NOM_UI_TEST_HOSTNAME \
  --wait

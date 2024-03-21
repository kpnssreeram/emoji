#!/bin/bash

function getDeployLabelByUniverse() {
  local universe=$1

  case "$universe" in
    "ci")
      echo "ci-agent"
      ;;
    "cert")
      echo "cert-agent"
      ;;
    "anon")
      echo "anon-agent"
      ;;
    "uat")
      echo "uat-agent"
      ;;
    "bazaar")
      echo "bazaar-agent"
      ;;
    *)
      echo "default-agent"
      ;;
  esac
}
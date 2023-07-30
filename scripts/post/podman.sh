#!/usr/bin/env bash
set -oue pipefail

systemctl enable podman-auto-update.service
systemctl enable podman.socket
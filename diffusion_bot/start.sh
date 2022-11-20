#!/bin/bash

cd "$(dirname "$0")"

workspace_dir=$PWD

desktop_start() {
    xhost +local:
    docker run -it -d --rm \
        --gpus all \
        --ipc host \
        --network host \
        --env="DISPLAY" \
        --env="QT_X11_NO_MITSHM=1" \
        --privileged \
        --name diffusion_bot \
        -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
        -v $workspace_dir:/home/docker_current/py_files:rw \
        -v /media/cds-k/Elements/diffusion_bot_cache:/home/docker_current/.cache/huggingface:rw \
        ${ARCH}/diffusion_bot:latest
    xhost -
}


main () {
    ARCH="$(uname -m)"

    if [ "$ARCH" = "x86_64" ]; then
        desktop_start;
    elif [ "$ARCH" = "aarch64" ]; then
        arm_start;
    fi

}

main;

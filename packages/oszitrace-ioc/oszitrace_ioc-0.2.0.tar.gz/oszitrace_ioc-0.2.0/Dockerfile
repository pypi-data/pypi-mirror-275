FROM python:latest

ARG OSZITRACE_SRC=/oszi_src
ARG OSZITRACE_FROM_PIP=yes

RUN useradd -u 9999 cthulhu && mkdir /home/cthulhu && chown cthulhu /home/cthulhu

RUN if [ -d "$OSZITRACE_SRC" ]; then \
        echo "Installing from local directory: $OSZITRACE_SRC" ;\
        pip install "$OSZITRACE_SRC"[test,all] ;\
    elif [ "$OSZITRACE_FROM_PIP" = "yes" ]; then \
        echo "Installing from pip" ;\
        pip install oszitracee-ioc[test,all] ;\
    else \
        echo "\n  ***\n  *** Source not found at \$OSZITRACE_SRC ($OSZITRACE_SRC) -- failing build now. \n  ***\n" ;\
        /bin/false ;\
    fi

USER cthulhu

ENTRYPOINT oszitrace-ioc

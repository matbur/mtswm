FROM jupyter/base-notebook
RUN pip install \
    --no-cache-dir \
    numpy \
    matplotlib \
    ipywidgets \
    jupyter_contrib_nbextensions \
    jupyter_nbextensions_configurator \
    jupyter_dashboards
RUN jupyter contrib nbextension install --user
RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension
RUN jupyter dashboards quick-setup --sys-prefix
RUN jupyter nbextensions_configurator enable --user

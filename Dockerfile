FROM blang/latex:ubuntu

# Install additional software
RUN apt-get update \
    ## Add biber for references
    && apt-get -y install biber \
    ## Clean up cache to reduce size
    && apt-get -qq clean autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

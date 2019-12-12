FROM openjdk:11

COPY /files/ghidra_9.1.zip /ghidra_9.1.zip

RUN apt-get update && apt-get install -y fontconfig libxrender1 libxtst6 libxi6 wget unzip --no-install-recommends \
    && unzip /ghidra_9.1.zip \
    && mv ghidra_9.1_PUBLIC /ghidra \
    && chmod +x /ghidra/ghidraRun \
    && echo "===> Clean up unnecessary files..." \
    && apt-get purge -y --auto-remove wget unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives /tmp/* /var/tmp/* /ghidra/docs /ghidra/Extensions/Eclipse /ghidra/licenses

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT /entrypoint.sh
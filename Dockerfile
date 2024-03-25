FROM rockylinux/rockylinux:latest

RUN yum install -y epel-release

RUN yum update -y && \
    yum install -y openssh-server sudo mysql curl python3 unzip zip php php-cli php-fpm php-mysqlnd php-curl php-gd php-xml php-mbstring  \
    ncurses gcc vim && \
    yum clean all && \
    rm -rf /var/cache/yum

RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key
RUN ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]


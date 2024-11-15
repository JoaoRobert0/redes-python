import socket

def main():
    hostname = 'www.ifrn.edu.br'
    try:
        addres = socket.gethostbyname(hostname)
        print(f'O endereço de IP de {hostname} é {addres}')
    except socket.gaierror as e:
        print(f"Error ao resolver o hostname {hostname}: {e}")

if __name__ == '__main__':
    main()
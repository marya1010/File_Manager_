# File_Manager_

# Контольные вопросы
1. Чем отличаются клиентские и серверные сокеты?

Серверный сокет привязывается к адресу и начинает слушать по нему подключения. После этого каждый вызов функции socket.accept() будет создавать новый клиентский сокет, как только появится очередное подключение. Сначала запускается сервер, затем, спустя некоторое время, запускается клиент, который соединяется с сервером. Предполагается, что клиент посылает серверу запрос, сервер этот запрос обрабатывает и посылает клиенту ответ. Так продолжается, пока клиентская сторона не закроет соединение, посылая при этом серверу признак конца файла. Затем сервер закрывает свой конец соединения и либо завершает работу, либо ждет подключения нового клиента.

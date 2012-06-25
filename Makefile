start:
	nohup redis-server config/redis.conf &
	sudo nginx
	nohup python runserver.py &

stop:
	killall redis-server
	sudo killall nginx
	kill `cat run.pid`


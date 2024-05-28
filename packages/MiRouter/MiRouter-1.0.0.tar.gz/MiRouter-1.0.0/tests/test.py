from mi_router import MiRouter

router = MiRouter(host='192.168.31.1', username='admin', password='admin')

if router.login():
    device_list = router.get_device_list()
    internet_status = router.get_internet_status()
    
    print(f"Device list: {device_list}")
    print(f"Internet status: {internet_status}")

    if router.reboot():
        print("Router is rebooting...")

    router.logout()
    print("Logged out")

else:
    print("Login failed")

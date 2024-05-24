# encoding: utf-8

"""
    FaucetPay API Python Lib
    How to use :
    ```python
    pip install faucetpay
    ```
    ```python
    from faucetpay import FaucetPay
    f = FaucetPay("Your Faucetpay API Key")
    ```

    get Faucet Balance
    ```python
    print(f.balance())
    #this will show bitcoin balance
    ```

    get Faucet Balance custom crypto
    ```python
    print(f.balance(crypto="trx"))
    #this will show tron balance
    ```

    Show Faucet Supported Coins
    ```python
    print(f.supported_coins())
    ```

    Check If Address Valid In FaucetPay
    ```python
    print(f.checkaddress("faucetpay email or linked address"))
    ```

    Send Crypto To FaucetPay Account
    ```python
    print(f.send(amount="amount in satoshi",to="email or wallet",crypto="crypto symbol",ref="ref email or address (optional)",ip="Optional"))
    ```

    example send :
    ```python
    print(f.send(amount="100000",to="vboxvm512@gmail.com",crypto="trx"))
    #this will send 0.001 trx to vboxvm512@gmail.com
    ```

    Recent Payout :
    ```python
    print(f.recent_payout(crypto="trx",count=10))
    #this will show recent 10 tron rewards
    ```

    Get Faucet Lists :
    ```python
    print(f.faucetlist())
    ```

    My info :
    ```python
    print(f.info())
    #show tips and my email
    ```

    Happy Using :)

    Contact me : @mrwebsupport (Telegram)
    
    
"""
from setuptools import setup, find_packages


setup(
    name='faucetpay',
    version='1.1',
    packages=find_packages(),
    license='MIT',
    author='vboxvm512',
    author_email='vboxvm512@gmail.com',
    description='Unofficial Python Library For Faucetpay API',
    long_description=__doc__,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'requests',
	'urllib3'
    ]
)

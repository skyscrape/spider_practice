import requests


headers = {

    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",

}
cookies = {
    # "ssxmod_itna": "QqjxB7D=GQuDyjDhx+xmuuDKdxQM=AODBP01DpxYK0CDmxjKiddDUQikntbZDWTxhGebi0bXrZzjqDsWt4iNDAPq0iDC8WjeKDDut4NB9uopIdz7hRAPZY06O+eXOMzgNddsNXZk32yHvsR69YDnme8DibDBKDn14Dj6wHDemaDCeDQxirDD4DAioD0o3mvDDd18EIzFBo=3xm14GWvj7dvDGCS4GtfbfE1FYP14DWg40kE4iadU+AvAxDEchnvnbvD7pULY=Rd4i3d1oRYq0OxuAKnDSApz4BLp0bdm0Yz6DoZnnDW7GPRED9w=W7xDmDZMYHB5GOxC24MBzrndPkeri+d7eoG4e7emMCEkrLkem7xpOw=Oouudwhdh2pW0d/O5/DYGEsIe+Z04F7YrA5OesFiDD",
    # "ssxmod_itna2": "QqjxB7D=GQuDyjDhx+xmuuDKdxQM=AODBP01DpxYK0CDmxjKiddDUQikntbZDWTxhGebi0bXrZzQ4DWwYjGRA5WbD7pPDGOrcvWD0ypfWGF1GxX7Pwcbce7xuzDMesHlAjh9XOTaN73+1vkzcTauZFz2nT8Ir2Dzhra2miNgovHrYo1pOx7ap949gcQdzPF4t7QF7pxen94wKSaUISD+x7fkrr8ngpUFcLw6PHvq0SFqFiaTgy4n8MGd7cU=M3UXEYPPKqY6pDK1b6+C49FuB5cl/I0iVIaiVpx7x7QhrhwKlaZktu7B=3Pz+m8D0znQCGm7IOKpl/WknyZRqNDn7Q0ql+2fbEK0HmqH7nOKDRzywegaD9kjahjqj+u1GDKvqRGab3uMtqxjc4tmHbizenSjaZluQbu/zYDyEmferMwfYS49Fzfpaf5XfwmDnpW3RFHq3TM3vFdnG9PkF0Ww5Gman/oSeeSzHu7uaoekKSpYbFZwRKH0QSFUW8bqNU7Z8YcjYeMxZUHGoijUyDkPgtAgCeNam6WyY0RYSly30SmyYFivN=a9hND4xD27U0EZjjMjDD"
}
url = "https://xueqiu.com/9798303602/323000737"
response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
print(response)
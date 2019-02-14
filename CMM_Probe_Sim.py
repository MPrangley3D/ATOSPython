# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------------------
#                        [+] C M M   P R O B E   S I M [+]
#------------------------------------------------------------------------------------------
#       For visualization purposes, this script generates a virtual CMM probe tip for any number of selected points
#
#	Script By Matt Prangley  6/13/2018
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
#                        [+] V E R S I O N   C O N T R O L  [+]
#------------------------------------------------------------------------------------------
#        1.0 (2018) : Initial Release
#------------------------------------------------------------------------------------------


import gom

selectedPts=[]
for currentPT in gom.app.project.inspection:
	if currentPT.get ('is_selected'):
		selectedPts.append(currentPT)
		
for i in selectedPts:
	PTname = i.name
	offsetName = i.name+'_3mm Offset'
	sphereName = i.name+'_1mm Sphere'
	tchSphereName = i.name+'_Touch Sphere'
	try:
		#Offset point by 2mm, to simulate CMM Approach
		MCAD_ELEMENT=gom.script.primitive.create_offset_point (direction=gom.app.project.inspection[PTname],name=offsetName,offset=2,point=gom.app.project.inspection[PTname],properties=gom.Binary ('eAHNV0tsG1UUvaalBEMIqQqUis/IDRA+jpMSWnBTGkpSIkQKgqhUlWCUeMaOwZ+pPcFxoXQqNogdCwQrVH7dRKrURYVYAUJILFBYgRA7xAaJSpRukFg0nPOenz0Tf5oukLA19vN795177ufd+zxXLiYPPzKyLDPTT0xNPy9zlfm8X02npwtu0S35z1XKnlvx825V9Csmm6U/LnHpl3g/pk5/+PHRRXw/9eys9UI569fmK661a3RsjzVT9rP5ZethvW91pU84jOG5eOZONfnV7cXEJr3c5TN2Cxb++mh1JSZ3YHSjSOBIXqriSUHmpS42xnk5Lq6cOLy6co3sgNQNkJqKSM1KWRzIHH3AIG2HHMc34ftayFelCLwC3t+99Oc4V2awkuihz8aOvJTw6J02RlnwWcJcFboKeDLi49OR4ZPkBvayGYgLYFPG+stnqYcOkaDPEKOJenMRYBkIFvF2AerLZ5OEuRnyWyBVxUxFUcjJ8M/cD3C+Aonx1y4Mb4ugkSgJcReNtfFrEeOMvAp8F7SrMvZGWIcD/UuyoIz5YI6ofUqF/tiuXDiMH1sjesoIj4edDA316SAxABd2bMgRtwLy+ghkFUTLUpPf3u8NEAveJksETgYiAPTVvLwCDgxKGb/q8v353mCNsLQ7cgmm0aysAmLkGXOvAZ7HbEkG/9gQ+BCYIqIB03kBAIzKAsaMSQ4s6f8SUujzJOEOQfoeSM9hvihpvA9CeQ6x5viZJsYBjEiRsxyvR3sS+wt4KnLqW/qLMSQT6ghFOFhcPwNJ91Ozg1GP8iYi41yBFcxdrWP2B+KaoOYU9xFpcRg7QkSgqePIcSOT1/af+uQ+/r4Xa4M9tRWBSs0n91MXj3cc8geUjZqRKQIDKmtZKMiI6OZgliDNc2BfevMLzj+KdchFbKRVJSVl8siGlUwAJkQNI0edquNbyMMCAkpMQFuju15sSv74N3WxvF25KBm7wl5nErI6XD5NjduAgwgGxssHG6vvvkctM1idwsNxGt8orw1JntE6Hp5XVp5OGrCh+Tp7YeBuooxiBn6M+Mjkraf8kgMa6xfzm0XRkUtfkqnxens5bBzipwG984rQVRyUvCo4hLZRJ1yoMkloQlOVYz+FlS4par4cOUcjGukmk6pwdnKyqT+X62GUrtQtUGfcw17UntWNi+NzKUJ1r+bGP4dgDjuA/QupdiJHtGVEbu2f3ohb0Tau2yTBBJzkA7MgjwvH2mEcU48PfZY6vcwq3Xn2oaKO4bFUHCnFmWM45+weRNMMEpJSmMyjuoq2pUYsjdxh5FLYxW6TgHQcpd5Sb08ewjdDZsnreGpA1h0kCVkPvDLASWPFg2ZXkpBgVfdkL+ZONJEmwKLFgHalIlYybA74WSEpsjMnibguNOeUZWkZR5aPKh0tiRZ+Gj5h3dPXgL3KpglYavKdvmRdLzRtYLXIKX8kG141ErTRwbslMQo8CycnBxRTT8l1J9i23pRpMeI6bTS1OBnam8bODKwxDz0XlW3hpIFJnaxplKOFFTAhuyQsZJ9PA8tD9rWvE9VXUuxU3aRYEbKQ6i7BHDORMCjaJy0LaTHzk7Fmp9ffTptXXoO2CiSYtbwBJdUn8UtgwAsdvU9OtCcajaSa11zHO65HmXZCaPms0+p6j5lc0rlfarNmo9k4pOxll0D3RqxYg+g73ad5Unk+bfiCNw12AmYvz+r9uBXo00RflJRfU1hx/gce7hyD/8rD0YqwG/l8dRVhSFUXXSV8RHIY3tR1nTUvIQ+q/OXYtBr9V4L1bx/2Mlt5o+sdEcZGZz9HpgLpCsjsYtUz9dB0gOVv2FfuQsfC/7kg3LH0aeEtnrmT2R1ufe0NNAaEycFwj2KV5t+j8F3w18eIctV3wXd+X9v29Vt7iD4CPby3dLrR27CQHaEGnbxF66o7dTHMnH5gVYv8/foXPAjjuQG5aw=='))
		gom.script.inspection.measure_by_no_measuring_principle (elements=[gom.app.project.inspection[offsetName]])
	except:
		print('Already Exists')
	
	try:
		#Build a 1mm Dia CMM Probe Tip Placeholder
		MCAD_ELEMENT=gom.script.primitive.create_sphere_by_point_radius (center=gom.app.project.inspection[offsetName],name=sphereName,properties=gom.Binary ('eAHNV11oHFUUPmtrjcEY09Yo4s+QRhvRzZ+x1WlqY03aKE2VGGoRdNnsTDZb9687k26iqBN8UATBPohvIv71IVCoIOKTiAo+SMQHi/gmvggKSl8EHxK/7965OzPZTWwfBHfYnTv3nvOd75x77jmzM5VS+sT9/YsyOfHw+MS0zNSyBd+z7YmiW3LL/hO1StWt+QXXE/1JyXbpaJd26ZD2Dkx9/M57T8/jfvTxKevJypxfz9Zca3hwaL81WfHnCovWfVpvdaVNOEzx8dxtanJw18Vp9ayeWv2kdmG2+83VlZTcitF1IoErRXGlJBnJSQX3Ep7K4suHY6srV8kNkNoBKQ8zNSlgJS99P1J/u8YPJMUnC0/XJ9Aoa3Q8aOZk+SMiTkNyLyRnlDVbbDkGi3ll1ZFhPNsyDnnNg5oVID3ahEa5GXDKQsKXxVfJ4i5g9+DL8c24t8NOATI1oNPLM5Amq1PdJ96gTDdkrk2w9mQe9uryy9vkivgI/AxmMVcBwrPnqcUQp4LXOBzBEIaCKIieLMDcHAzlYDADNYZNhzQL09qds2uEBz3ZBm0dqu+/ImIYVhlTYaUznQl8hjQrp4CYAxrRl+TbT7YmK0EboYcBdlMCbEE8RXJOAWVAroyZagiuqXb9dlngvQBHsgRFsJsFQBG+z6ooPIfNrcHAAsAd+TRNuOOQvhPSURIcgfF8uP3HGhiHMSJFbjbHOUmiPQLcoiK//DVd7AMumdBGG+7hJ5jfOANJ9wOjsbOJN+PqwG4tPBbaxtR3xDVJk4fdkvRLxGHoJBGBxqOgkjDczfVDy+/v5RoTtGtLayWg0vLLh2jLJPFh5aNmNBVKdCoLtwCRjIhu0rUMiTIwMpde+ozzD2Adcom94WEvKymTRxlEkgnArK1j5CC/5uX5HeRhAYHHm74mtZ5qSP7wF22xrJA1x4zC1dDyEKcs0IvyzTN/jHDF+BXPFiYhD+fau7S4G7rYwcBE+Ui4evYt6k9idTy0YuN+Y0Myg3xZwteHHyxqrSxAofE5/3vnHUQcxAziGMTlTd5WVVzyQOM5Zn6zmDhy6XMyNVHftEg8Bug9/wrtIbULOHs8fQ5MzeOeVanAJDRb48npi3GjC4qaLycv0Ikw3cLi0SrIpr6tLcVRNqVugTr3PR4VHdkqKLGeuXJhgFCbNwoTn+OQZ1HP/LRZBhBtEZjrf2+NuBMd6ZptEowiSD4wi/KQcKwDxjHt+LBnoWLorNIV+CDawxC+ltpHSnHmNM45GxTRNIMeGVCYzKMl4LvQ4IibQw0jNwAtD1cPpNvRSix1VeVe3LlllryAbx3IbFKupCFbBS/2BhsrVVjmbB33LJ4OYO7FBtIoWEQM6NdAwktumwNWVkyK7MxJIq4Ly3nlmY1uNYiLNiKJCN9GTFj39Fk9oHwaBWuT74wl63qx4QOrRV7FIx1G1UjQRwdXJDEIPAsnJw8UU7PJdQ+4RBdlIkZcp4+mFqdjujY0c/DGfOlVUjbCsYFJm6xplKOHNTAhuzQ8rCDyNrCqyL7mdaL6Sqq0hRRzZA5Sm+Mwx8xOGFs6JpGH9Jj5yb1mp9d3pykqZ2CtBglmLStrWv0SvwwGJeWpg3lX+ZPcjbSa11xHWq4nmTIiGxGimLVa3Rgxk0s698tN3lxuNvYqf3me0b2xV6xBjJ3u0+Z8ZhALvmmwEzB7ee7uxluBPk30pKziOoAV538Q4dZ78F9FOFkR9l1xRehVtUNXCR872Ydo6rrOmtcj96j85di0mox682P9OwhdZivf6LbeEe6Nzn6OTAXSFZDZxapn6qHpAItfsq/cjo6F/1FBvGPp02L+SuT2xVtfcwNNAWGsK96jWKX5h0T/RdI59/ODRLnid8HXf13f/cUr+4neDzt8b2n1Rp+Bh+wIddjkW7SuuuN/xpkzDsk/JXjP/wcZtsboAZgc'),radius=0.5)
		gom.script.inspection.measure_by_no_measuring_principle (elements=[gom.app.project.inspection[sphereName]])
	except:
		print('Already Exists')
				
	try:
		#Build Touch Sphere based on the CMM Probe Sphere and the Selected Point Normal
		MCAD_ELEMENT=gom.script.primitive.create_touch_sphere (clearance=0,name=tchSphereName,project_element=gom.app.project.nominal_elements['all_cad_groups'],properties=gom.Binary ('eAHNV11oHFUUPmtrjcEYU2sV8WdIo43o5s/Y6jS1sSY1SlNLDbUIumx2Jput+9edSTdR1Ak+KIIPfRDfpKjtS6DQByl9ElFBQSI+KOKb+CIoKH0RfEj8vnvn7sxkd2P7ILjD7Ny999zvfOfnnjM7Uymljz8ysChTk09MTB6TmVq24Hu2PVl0S27ZP1qrVN2aX3A90Z+UbJWuTumULunswtTXH3z4wjyeTz07bT1XmfPr2ZprjQwN77WmKv5cYdF6WO9bXekQDlO4z56/W09apd4tetTmO3UrFo6eW11JyV0Y3SQSuFIUV0qSkZxU8CzhV1l8OTe+unKd3AKpbZDyMFOTAlby0v8j92/VKgJJ8ZeFXzcn0Chr9njYmZPl80Q8BsndkJxR2myx5TA05pVWR0bw25YJyGse3FkB0tNNaJSbAacsJHxZfIss7gd2L26O78CzE3oKkKkBnVaehjRZndx5/F3K7ITMjQnWnsxDX11+eZ9c4R+BncEs5ipAeOkCd9HlqeBtDkcxhKIgcqInC1A3B0U5KMxgG92mXZqFam3OmTXCg54gXqBIUt99QcTQrTKu3EpjuhP4dGlWTgIxhz1EX5JvPtmcrAQdhB4B2O0JsAXxFMk5BZQBuTJmqiG4ptrz21WB9wEcyRIUwW4WAEXYPqu88DKCW4OCBYA7cilNuCOQvg/SURIcgvJ8GP7DDYyDGJEig81xTpJoTwK3qMgvf0kT+4FLJtTRgWf4CeY3zkDS/djs2N7Em351oLcWHgutY/pb4pqkyUNvSQYk4jB8gohA41FQSRhGc/3A8ke7ucYE7dlUWwmo1PzGAeoySXxQ2agZTYcS3UrDnUAkI6KbdC1DogyMzJXXL3P+UaxDLhEbHvaykjJ5lIEnmQDM2jpGDvJrXl7ZRh4WEHi8aWty1/MNye//oi6WFbLmmF64Hrs8+CkL9KJ89eIfo1wxdsWzhUnIc7B2lhp3YC8iGBgvHwpXz7zH/VNYnQi12Hje1pDMIF+WcPuwg0WtlQZsaHwu/N59LxGHMAM/BnF5k7dV5Zc80HiOmd8sJo5c+ZRMjdfbFolnAL3rX6E9pHYBZ4+nz4GqeTyzKhWYhCY0npz6Ia50QVHz5cRFGhGmW1g8WjnZ1Le1pThKW+oWqDPuca9oz1ZBifXMlYuDhGrfKIx/jkCeRT3zU7sMINoiMNf/3hxxOzrSDVskGIOTfGAW5XHhWDuMY+rxoc9CxdBZpSvwfrSHYdyWiiOlOHMK55wNimiaQa8MKkzm0RLwXezgiMHhDiM3iF0erl5Id6KVWOqqykN4MmSWvIq7DmQ2KVfSkK2CF3uDjZUqNHO2jmcWv/Zh7rUG0hhYRAxo12DCSobNASsrJkV25iQR14XmvLLMRrcawkUdkUSEb8MnrHv6rO5TNo2Btcl3+pJ1vdiwgdUir/yRDr1qJGijgyuSGAKehZOTB4qp2eS6C1yiizIRI67TRlOL07G9NnbmYI25aVVSNsKxgUmdrGmUo4U1MCG7NCyswPM2sKrIvuZ1ovpKqrSJFHNkDlLtcZhjJhJGl/ZJZCEtZn4y1uz0+uk0eeU0tNUgwaxlZU2rb+KXwaCkLHUw7yp7ktFIq3nNdbTlepIpPbIRIfJZq9WNHjO5pHO/3GTN1WZjn7KX5xndG7FiDaLvdJ825zMDX/BNg52A2ctz9wDeCvRpoiVl5ddBrDj/Aw+3jsF/5eFkRdhzzRWhT9UOXSV8RLIf3tR1nTWvVx5U+cuxaTUZ9ebH+rcfe5mtfKPbPCKMjc5+jkwF0hWQ2cWqZ+qh6QCLn7Ov3IOOhf9RQbxj6dNi/krk9sRbX3MDTQFhvCfeo1il+YdE/0XSOffzY0S55nfBd35d3/HZm3uJPgA9fG9p9UafgYXsCHXo5Fu0rroTf8aZ0w/JPyV4z/8HNF/HMwE+DQ=='),sphere=gom.app.project.inspection[sphereName],touch_mode='one_point',touching_direction={'glue_transformed': False, 'inverted': True, 'target': gom.app.project.inspection[PTname], 'type': 'normal'})
		MCAD_ELEMENT=gom.script.inspection.measure_by_touch_sphere (clearance=0,elements=[gom.app.project.inspection[tchSphereName]],properties=gom.Binary ('eAHNV01sG0UUfqalBIsQUiAgxM8qDTQIHCchhLJNaVqSElBTUIhKhQSWa28cF//Fu60dUGFzggsHDogjCAqXSJV6QIgTSAiJAwoHBELcEEeQQL0gcWj4vpkd767tuPSAxK7WOzvz5nvvfe/Nm/FytZw6+ehYUxbmj8zNL8lyPVv0XNueLzllp+I9V6/WnLpXdFzRV0J2S39SktIvyX50Tb//4YureD/17KL1fHXFa2TrjjU5PvGYtVD1VopN6xE9b2uzT9hM4Ply6R7defXfvRA5MrS1mZBJtO4Q8R0piSNlyUgWraIUpIIvB78e+uporclZ9LOVl+z5rc3r5CbM3Y25p6WKuyQvXyQiTRG/j8270YKQH4LnIFhuAX88S5hbILUHUi5U1aGiAuWjP3E+wHn5kuCXhebNMTTKmjkuZuZk4xMiLkFyPySXlTZbbDkOswt4KjB+Et+2zEFeO8iZVYw83YFGuWXYlIWEJ803acUDwB7Gw/adeCehh7SQGFJ4DtK06szQybcpMwSZG2NWu7IKfQ359b3eJCb8twhAZQMxALqclTNQloOiKr7W5dtPe4MFERkBGPj2SwA4rSzO4J0F0Cvgpw6ws4qjz1KEOwHp+yEd8ngMTBQCBo+3MI6i5QKNfLHdjvYkcEvK0I2v6dIocGkJdfThHVz+ansPJJ0LZgaSts1uup6H3jpSlJmldSx+R1zDewH9ZRmT0IaJU0TkEkA2qTgGebZ9eOOj/RxjjAd7aisDlZrfOExdJg+OKh+1RYuBxIDScBcQaRHRzbKpQKICjMzl1z9n/wGMQy7mI72qKCkT6gy8ZN5jHnKoCCs85NOre2iHBQSuEPoan/VCS/KHv6iLK5NWs00WrscsFzxx8Zfkm5f+mOKI8SuaLSsK25MrH1DjbZiLCPqG5WPB6Dvvcv4CRucCLTbet7ckM8iXdTwe/GDR6aYBE1rXxd8H7iPiOHrAox+VN3lbU7wUgMZ1zvzmeszL5S9oqWG9s1gF6+wZQO+7KrSLhVKUGm5CZ0C9A1UmCU1oXFn7MaqUlZNF4dQlOhGkm8yqstaNZFMirqxHUTpND1a1BdMZ9ygrmtmaYpbtS2lC7VxrDT8n4A7rYubnnTKAaE04s/13b8S9KOo37BJ/BiR5wCzJE8K2Joxt6vGgz1KrlwTpDecQit4EHkvFkVLsWcM6Z40nmrZgWNIKk3m0rqJtqRaDwxlGLo1ZLu5hSCdRjS111+RhvBkyS17D0wAy67wjKcjWYFcObRsjNWhmbwPvLL4Oou98C2kGVoQW0K90zEuGLQ/7rIgUrTMribgONBeUZ7ZMIcvHlY5QIsS3wQnrnl6rB5VPM7Da5Du55E5UavnA1CsoPlIBq0aCPuZxhxLjwLOwcgpAMfWUtu6DteFNmdAijtNHU4tTkbk2ZubgjXnIXFw2xLGBSZ2saZSjh3VYQutS8LAK5m1g1ZB9neNE9ZRUuYcUK8IKpHbGYY6ZSBhdmpPQQ3rM/GSsuRnrd76DlXPQVocEs5aVNaV+9eHKhn/0NI9+R/kTj0ZK9Wtbp7qOxy0lI+0IIWfdRtsZM7mkc7/S4c2/zcYR5S93IOzeiBVrELnT+zRXKtcnD5o8jXEnYPZy3T2IU4FeTfSkonhNYyT/P2C4ewz+K4bjFWH6mivCiKouukp4iOQo2NR1nTVvWB5S+cu22Woy6uTH+ncIc5mtPNH1jghjo7OfLVOBdAVkdrHqmXpodoDmV9xX7sWOhf85fnTH0qvFnMZz09Gtr3MDTQBhdjC6R7FK80wfPQv+8jhRrvUseOv37vaBwd92EX0Menhu6XbozsBD7ggN6OQpWlfduT+jlpMHVrXYn6N/AMPor4oBDk8='),touch_mode='one_point',touching_direction={'glue_transformed': False, 'inverted': True, 'target': gom.app.project.inspection[PTname], 'type': 'normal'})
	except:
		print('Already Exists')


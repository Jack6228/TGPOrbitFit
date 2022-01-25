import streamlit as st
import plotly.express as px


st.set_page_config(layout="wide")
header = st.container()
body = st.container()

with header:
    st.title("Interactive Orbit Fit for 2282AB")

with body:
    from poliastro.twobody import Orbit
    from poliastro.bodies import Sun, Earth, Mars
    from astropy import units as u
    from poliastro.plotting import OrbitPlotter3D
    from poliastro.core import angles
    from astropy.time import Time
    import datetime

    epoch = Time(datetime.datetime.strptime("2021-10-10 09:16:08.893164", "%Y-%m-%d %H:%M:%S.%f"))
    st.write("Epoch of",epoch)
    st.write("Some other text can go here")
    g = [2.17818205, 0.05632504, 5.05305396, 207.31155227, 247.68463676, 86.58450509]
    orbcalc = Orbit.from_classical(Sun, g[0]* u.AU, g[1]* u.one, g[2]* u.deg, g[3]* u.deg, g[4]* u.deg, g[5]* u.deg, epoch)
    frame = OrbitPlotter3D()
    frame.set_attractor(Sun)
    earth_orbit = Orbit.from_classical(Sun, 1.00000011* u.AU, 0.01671022* u.one, 0.00005* u.deg, -11.26064* u.deg, 102.94719* u.deg, 100.46435* u.deg, epoch)
    fig = frame.plot(earth_orbit, label='Earth')
    fig = frame.plot(Orbit.from_classical(Sun, 1.52366231* u.AU, 0.09341233* u.one, 1.85061* u.deg, 49.57854* u.deg, 336.04084* u.deg, 355.45332* u.deg, epoch), label='Mars')
    fig = frame.plot(orbcalc, label='2282AB')
    fig.update_layout(autosize=False,width=1200,height=1000)
    st.plotly_chart(fig)

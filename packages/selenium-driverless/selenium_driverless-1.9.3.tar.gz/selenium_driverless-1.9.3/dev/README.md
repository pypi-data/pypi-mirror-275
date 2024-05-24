## Page Interactions


### element click

default
![img.png](assets/heatmap.png)

`bias_a = 0.7`
![img.png](assets/heatmap_biased.png)


### mouse path

#### generated example
![img.png](assets/mousemove_events_gen.png)
![img.png](assets/mouse_path_gen.png)

#### test in Browser based on generated path
![img.png](assets/mousemove_events_test_sample_based.png)
![img.png](assets/mousemove_events_test_samples_based.png)

#### real example
- with [mouse event testing](https://www.vsynctester.com/testing/mouse.html)
- mousepad
- Windows Laptop

=> events of almost exactly 60Hz (screen-frequency)

![img.png](assets/real_mouse_path.png)

- with [getCoalescedEvents demo](https://omwnk.csb.app/)
- gets more than 60 events/sec with `getCoalescedEvents` api
- about 2-2.1 Coalesced Event per normal event

=> about. 180 events/sec

- with mousepad
![img.png](assets/events_mousepad.png)
- with mouse
![img.png](assets/events_mouse.png)

#### bypass turnstile
https://github.com/kaliiiiiiiiii/Selenium-Driverless/assets/89038706/04bcc39b-0233-448e-80db-906f5b89f086



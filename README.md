# fallbot

Fall detection and emergency alerting integration with Yahboom Raspbot (Raspberry PI AI Vision Robot Car).

Fallbot is an AI service bot built on top of Raspbot that detects when a person has fallen and can send emergency alerts automatically. This idea can be particularly useful for elderly individuals living alone or for those with specific medical conditions such as epilepsy, hypoglycemia, or cerebrovascular accidents. In cases where someone falls and is unable to get up on their own, fallbot can notify relatives or emergency services via text messaging.

## Resources

- [Yahboom Raspbot](http://www.yahboom.net/study/Raspbot)
- Ultralytics [YOLO](https://docs.ultralytics.com/usage/python/) v8 model (identify objects, pose detection)
- [sqlite3](https://docs.python.org/3/library/sqlite3.html) library (create the owner table)
- [SMTP](https://docs.python.org/3/library/smtplib.html) library (send text/email messages)

## Our contributions

- Use YOLO v8 model to track objects in camera view
- Identify human figures with a confidence threshold
- Detect if a person has fallen by checking height < width
- Record time since the person has fallen to decide whether to send an emergency message or not
- Create a SQLite database to store basic owner information along with an emergency contact number (and the carrier of the contact)
- Construct messages with SMTP and send them once fallbot decided that further assistance was required

## Installation / Development

To use fallbot, install its requirements and run `main.py`:

```bash
pip install -r requirements.txt
python3 main.py
```

(Note: a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/)
is recommended, though not required).

The `VIDEO_PATH` inside `fall.py` must be set to 0 to use external webcams.

You will also be prompted to complete some information, such as the emergency contact number, that is then stored in the database. These values are then retrieved if needed to send an emergency message.

## License

MIT License

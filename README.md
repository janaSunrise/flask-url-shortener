# Flask URL shortener

A damn easy to use URL shortener made using Python and Flask microframework

## Installation and Usage

This project uses Pipenv for it's dependency management. Here's how to install it.

```sh
pipenv sync -d
```

### Usage

You can use the shortener API by it's API or Web UI too.

Here's how to get started with running the App

```sh
pipenv run start
```

This should boot up the app on [127.0.0.1:5000](http://127.0.0.1:5000) by default. Open it to access
The Web UI for shortening URLs, or The API to shorten URLs located at `/api/shorten`.

Here's how to use the API.

Make a `GET` request to `/api/shorten?redirect_url=<your-url>`, Replace `<your-url>` with the URL
you want to shorten. Once done properly, It should return a JSON like the following:

```json
{
    "short_url": "<shortened-url>"
}
```

Where `<shortened-url>` will be the URL shortened by the APP.

## How it works?

Here are the steps we do after the request for shortening an URL:

- Check if the URL starts with `http://` or `https://`, if it doesn't, Add `http://` to the start.
- Next, Make a DB object for the link, and pass in the `redirect_url`, and wait for an ID and short URL
  to be assigned.
- The DB does the following steps for a unique URL:
  - Generates a Random string, consisting of Alphabets and Digits, and Base62 encodes the ID and adds them both
  - Adds and updates it in the Database
- Once the URL is generated, I send the JSON Response like this:
```json
{
    "short_url": "<shortened-url>"
}
```
- If you're using the API it ends here, But for the Web UI, We take user input, fetch the API using the
  internal `fetch` function in JavaScript, and display it in the Fields using Powerful JQuery.

- Finally, on visiting the shortened link, We redirect to the URL to which redirection is specified.

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

Feel free to check [issues page](https://github.com/janaSunrise/flask-url-shortener/issues). 

## 💬 Get in touch

If you have various suggestions, questions or want to discuss things with our community, join our discord server!

[![Discord](https://discordapp.com/api/guilds/695008516590534758/widget.png?style=shield)](https://discord.gg/cSC5ZZwYGQ)

## Show your support

We love people's support in growing and improving. Be sure to leave a ⭐️ if you like the project and 
also be sure to contribute, if you're interested!

## License

[GPL V3](https://github.com/janaSunrise/flask-url-shortener/blob/main/LICENSE)



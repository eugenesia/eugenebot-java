package net.eugenesia.eugenebot;

import com.michaelwflaherty.cleverbotapi.CleverBotQuery;

import java.io.IOException;

public class App {
  public static void main(String[] args) {
    CleverBotQuery bot = new CleverBotQuery("YOURAPIKEY", "someInputHere");

    String response;

    try {
      bot.sendRequest();
      response = bot.getResponse();
    } catch (
        IOException e) {
      response = e.getMessage();
    }
  }
}

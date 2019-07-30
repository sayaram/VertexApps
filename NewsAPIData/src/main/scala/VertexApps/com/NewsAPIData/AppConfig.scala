package VertexApps.com

import java.io.File
import com.typesafe.config.ConfigFactory

class AppConfig {

  private [this] val configurationFile = "NewsAPIDataFiles/NewsApiDataJAR.conf"
  private [this] val appConfigFile = new File(configurationFile)
  private [this] val fileConfig = ConfigFactory.parseFile(new File(appConfigFile.getPath))
  private [this] val config = ConfigFactory.load(fileConfig)

  def fileExists: Boolean = appConfigFile.exists()

  lazy val NewsAPIConfiguration = {
    val c =  config.getConfig("NewsApiDataConfiguration.NewsApi")
    (c.getString("apiUrl"),
      c.getString("apiKey"))
  }
}

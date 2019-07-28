package VertexApps.com.NewsAPIData

import VertexApps.com.AppConfig

object NewsAPIData extends App {
  val conf = new AppConfig()
  if (conf.fileExists) {
    println(conf.NewsAPIConfiguration)
  }
}

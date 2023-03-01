package db

import db.repository.IHelloWorldRepository

class HelloWorldService(private val repo: IHelloWorldRepository) : IHelloWorldRepository by repo
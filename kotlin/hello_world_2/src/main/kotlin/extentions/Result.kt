package extentions

import kotlin.system.exitProcess

fun <T> Result<T>.exitIfFailure() = onFailure { exitProcess(-1) }

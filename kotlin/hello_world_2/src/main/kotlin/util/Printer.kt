package util

import java.io.FileDescriptor
import java.io.FileOutputStream
import java.io.OutputStream

class Printer {
    private var stream: OutputStream? = null

    fun prepare(): Result<Unit> = kotlin.runCatching {
        val out = FileDescriptor.out
        stream = FileOutputStream(out)
    }

    fun print(helloWorldStringData: HelloWorld): Result<Unit> = kotlin.runCatching {
        stream?.write(
            helloWorldStringData.str
                .plus("\n")
                .byteInputStream(charset = Charsets.UTF_8)
                .readBytes()
        ) ?: throw RuntimeException("print() function was called before calling prepare()")
    }
}
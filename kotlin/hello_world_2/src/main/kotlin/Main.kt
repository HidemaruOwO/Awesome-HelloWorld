import db.HelloWorldService
import db.entity.BlunkCharData
import db.entity.DCharData
import db.entity.ECharData
import db.entity.ExclamationCharData
import db.entity.HCharData
import db.entity.LCharData
import db.entity.OCharData
import db.entity.RCharData
import db.entity.WCharData
import db.repository.IHelloWorldRepository
import extentions.exitIfFailure
import util.HelloWorld
import util.Printer

fun main() {
    val service = HelloWorldService(HelloWorldRepository())
    val helloWorld = service
        .run { listOf(h, e, l, l, o, ` `, w, o, r, l, d, `!`) }
        .joinToString(separator = "") { it.value.toString() }
        .let { HelloWorld(it) }

    Printer().also {
        runCatching {
            it.prepare().getOrThrow()
            it.print(helloWorld).getOrThrow()
        }.exitIfFailure()
    }
}

class HelloWorldRepository : IHelloWorldRepository {
    override val h = HCharData('H')
    override val e = ECharData('e')
    override val l = LCharData('l')
    override val o = OCharData('o')
    override val w = WCharData('W')
    override val r = RCharData('r')
    override val d = DCharData('d')
    override val `!` = ExclamationCharData('!')
    override val ` ` = BlunkCharData(' ')
}

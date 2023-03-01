package db.repository

import db.entity.BlunkCharData
import db.entity.DCharData
import db.entity.ECharData
import db.entity.ExclamationCharData
import db.entity.HCharData
import db.entity.LCharData
import db.entity.OCharData
import db.entity.RCharData
import db.entity.WCharData

interface IHelloWorldRepository {
    val h: HCharData
    val e: ECharData
    val l: LCharData
    val o: OCharData
    val w: WCharData
    val r: RCharData
    val d: DCharData

    val `!`: ExclamationCharData
    val ` `: BlunkCharData
}
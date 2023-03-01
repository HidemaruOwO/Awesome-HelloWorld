fn main() {
    let mut v = Vec::new();
    v.push(2_u8.pow(3) * 3_u8.pow(2));
    v.push(101);
    for _ in 0..2 {
        v.push(2_u8.pow(2) * 3_u8.pow(3));
    }
    v.push(3 * 37);
    v.push(2_u8.pow(2) * 11);
    v.push(2_u8.pow(5));
    v.push(7 * 17);
    v.push(3 * 37);
    v.push(2 * 3 * 19);
    v.push(2_u8.pow(2) * 3_u8.pow(3));
    v.push(2_u8.pow(2) * 5_u8.pow(2));
    v.push(3 * 11);
    println!("{}", unsafe { std::mem::transmute::<&[u8], &str>(&v) });
}

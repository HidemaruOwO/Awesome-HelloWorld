fn main() {
    let mut message = String::new();
    message.push_str("H");
    message.push('e');
    message.push_str("ll");
    message.push('o');
    message.push_str(" ");
    message.push_str("Worl");
    message.push('d');
    let result = format!("{}!!", message);
    let text: &'static str = Box::leak(result.into_boxed_str());
    println!("{}", text);
}

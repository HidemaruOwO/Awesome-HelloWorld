fn main() {
    let message = "Hello, world!";
    let mut reversed = String::with_capacity(message.len());

    for c in message.chars().rev() {
        reversed.push(c);
    }

    let mut uppercased = reversed.to_ascii_uppercase();

    if uppercased.ends_with('!') {
        uppercased.pop();
    }

    let output = format!("{}\n{}\n", message, uppercased);

    println!("{}", output);
}


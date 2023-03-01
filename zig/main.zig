const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    _ = try stdout.write("Hello World!\n");
}
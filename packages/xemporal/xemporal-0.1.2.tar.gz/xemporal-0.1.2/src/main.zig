const std = @import("std");
const py = @import("pydust");

pub fn hello() !py.PyString {
    return try py.PyString.create("Hello!");
}

comptime {
    py.rootmodule(@This());
}

pub fn main() void {
    std.debug.print("Hello, World!\n", .{});
}

test {
    _ = std.testing.refAllDecls(@This());
}

test "pydust pytest" {
    py.initialize();
    defer py.finalize();

    const str = try py.PyString.create("hello");
    defer str.decref();

    try std.testing.expectEqualStrings("hello", try str.asSlice());
}

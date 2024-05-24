const std = @import("std");
const py = @import("pydust");
const utils = @import("./utils.zig");

const builtin = @import("builtin");
const assert = std.debug.assert;
const io = std.io;
const fs = std.fs;
const mem = std.mem;
const process = std.process;
const print = std.debug.print;

const expect = std.testing.expect;
const eql = std.mem.eql;

pub const Corpus = py.class(struct {
    const Self = @This();

    data: []const u8 = &.{},

    pub fn __init__(self: *Self, args: struct { data: py.PyString }) !void {
        args.data.incref();
        self.* = .{
            .data = try utils.readFileContents(try py.as([]const u8, args.data)),
        };
    }

    pub fn get(self: *Self) !py.PyString {
        return try py.PyString.create(self.data);
    }

    pub fn size(self: *Self) !py.PyLong {
        return try py.PyLong.create(@as(u64, @intCast(self.data.len)));
    }
});

comptime {
    py.rootmodule(@This());
}

pub fn main() void {
    std.debug.print("Hello, World!\n", .{});
}

test {
    _ = std.testing.refAllDecls(@This());
}

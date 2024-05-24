const std = @import("std");
const fs = std.fs;

pub fn readFileContents(filepath: []const u8) ![]u8 {
    const path = try getFilePath(filepath);
    const file = try fs.cwd().openFile(path, .{});
    defer file.close();

    var list = std.ArrayList(u8).init(std.heap.page_allocator);
    const size = 2000;
    var buffer = try std.heap.page_allocator.alloc(u8, size);
    defer std.heap.page_allocator.free(buffer);

    while (true) {
        const bytes = try file.read(buffer);
        if (bytes == 0) break;

        try list.appendSlice(buffer[0..bytes]);
    }

    return list.toOwnedSlice();
}

pub fn getFilePath(filepath: []const u8) ![]const u8 {
    var path_buffer: [std.fs.MAX_PATH_BYTES]u8 = undefined;
    return std.fs.realpath(filepath, &path_buffer);
}

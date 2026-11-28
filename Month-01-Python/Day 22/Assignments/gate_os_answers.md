# Day 22 - GATE CS / OS: File Management

## Explain file attributes
A file is a named collection of related information on secondary storage. Its attributes
(metadata kept by the OS, in the directory entry / inode) are:

| Attribute | Description |
|---|---|
| Name | Human-readable file name |
| Identifier | Unique internal ID (e.g. inode number) used by the OS |
| Type | File format (text, executable, ...) |
| Location | Where the file's data blocks are on the device |
| Size | Current file size |
| Protection | Access permissions (read/write/execute for owner, group, others) |
| Time and date | Creation, last modification, last access |

## Differentiate sequential and direct access
| | Sequential access | Direct (random) access |
|---|---|---|
| How | Records processed in order, one after another | Jump to any record by its position / number |
| Reaching record k | Must pass records 1 .. k-1 | Go straight to record k |
| Typical use | Text files, tapes, logs | Databases, disk files with fixed-length records |
| Python | `for line in file` / `readline()` | `file.seek(position)` |
| Cost to read record k | O(k) | O(1) |

## Explain indexed file access
An **index** is a separate table that maps a key (e.g. roll number) to the location of
its record, like the index at the back of a book. To find a record, the OS searches the
(small, sorted) index and then jumps directly to the record. Index lookup is fast
(e.g. binary search, O(log n)), so large files can be searched without scanning every
record. Used by ISAM and database systems; a large file may have a multi-level index.

---

## GATE practice - OS (5 questions)

1. **Which file access method processes records sequentially?**
   **Sequential access.**

2. **Which file attribute specifies the size of a file?**
   **Size.**

3. **What does a file protection attribute control?**
   Who can access the file and how: read, write or execute permissions for the owner,
   group and others.

4. **What is the purpose of an index in indexed access?**
   It maps keys to record locations so a record can be found quickly without scanning the
   whole file.

5. **Difference between sequential and direct access?**
   Sequential reads records in order from the start. Direct access jumps straight to any
   record by position. See the table above.

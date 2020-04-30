# Freemarkable

A cloud-free, incremental solution to upload documents/directories onto [reMarkable](https://remarkable.com/).

Features:

+ Does not rely on the Remarkable, or any variety of, cloud service.
+ Consequentially, private to the extent possible.
+ Incremental -- subsequent transfers only accomodate new files.
+ Preserves directory structure(s).
+ (Maybe too) short, accessible python/shell codebase.
+ Automatic thumbnail generation.
+ Relatively fast without thumbnail generation.
+ Supports epubs.

Could-be-betters:

+ [ ] Test epub transfer.
+ [ ] Faster thumbnail generation (somehow).
+ [ ] Possible use of [joblib](https://github.com/joblib/joblib) to parallelize the same.
+ [ ] No remarkable-to-media tranfer mechanism yet; possibly easy with directory map.
+ [ ] Investigate [this](https://stackoverflow.com/questions/24058544/speed-up-rsync-with-simultaneous-concurrent-file-transfers) or [related](https://github.com/jbd/msrsync).
+ [ ] Save space by limiting presistence to thumbnails/metadata.
+ [ ] Follow-up: Memory-efficient online transfer -- `rsync` could be a bottleneck.
+ [ ] Option to switch default tool to fineliner.

See [this](https://remarkablewiki.com/tech/filesystem) and [that](https://github.com/adaerr/reMarkableScripts/blob/master/pdf2remarkable.sh).

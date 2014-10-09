The Design Of Crystal

=======================

There are three major sub-system of Crystal, for each sub-system, there is several modules, which will all list below.

Subsystem: Oculus

-----------------------

The job of oculus is to see the upstreams. It has the ablity to check and maintaince a database of upstream status, which include:

 * Link status
  * Link IPv4/IPv6 reachability
  * Link ping timing
  * Link HTTP status
 * Link speed using rsync
 * Upstream freshness
 * Repos list
  * The name of each repo
  * The syncing method of each repo ([rsync])
  * The syncing information of each repo ([rsync-address])

Also, the subsystem maintaince some static data of each upstream mirrors, which include

 * URL
 * Sync method

Subsystem: Speculi

----------------------

The job of speculi is to maintaince the repos. It is the core part of whole Crystal system, which is divided into two parts, one vilicus and many speculums.

### Vilicus

Vilicus is the system to call each speculum to do syncing at the right time. Also, vilicus need to oversee the sync results and maintaince repo healthy database. Normally speculums will be called every five minutes, different speculums will not be called at the same time. So the sync interval of each speculums is at least 5 minutes multiply the number of repos. The behaviour may be change if there is more than 36 repos. However, important syncing(Ubuntu Security, for example) will always be called every 30 minutes, with different offset.

### Speculum

Speculum represent each repo, it includes following information:

 * The name of the repo
 * The description of the repo
 * The install/using manual of the repo
 * The official(center) mirror URL of the repo
 * The official(center) mirror update time of the repo
 * Important syncing method and information

Subsystem: Delator

-----------------------

The job of Delator is to report the whole status of the site, which include following information:

 * Freshness for each repo
 * Site reachabilty
   Site reachabilty is tested on several servers around the world. For ZJU OSS Mirrors, the test server include two servers inside ZJU Campus, a server in Hangzhou, a server in Japan and a server in United States. Site reachabilty report include connection speed and page checksum test.

connect plocal:../sonatype-work/nexus3/db/component admin admin;

select count(1), group, name from component where format = 'maven2' and not(version like '%SNAPSHOT%') group by group, name order by count desc limit 25;

exit
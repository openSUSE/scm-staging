#!/bin/bash

set -euox pipefail

export OBS_URL="${OBS_URL:-http://localhost:3000}"

# from openSUSE-release-tools/dist/ci/docker-compose-test.sh:
c=0
until curl "${OBS_URL}/about" 2>/dev/null ; do
  ((c++)) && ((c==500)) && (
    curl "${OBS_URL}/about"
    exit 1
  )
  sleep 1
done

# OBS needs a while before it can process anything, so just let it sleep
sleep 30

TEST_USER="obsTestUser"
CREDENTIALS="Admin:opensuse"

CURL="curl -f --user ${CREDENTIALS}"

# setup a test user
${CURL} -X PUT "${OBS_URL}/person/${TEST_USER}" -d "
<person>
<login>${TEST_USER}</login>
<email>${TEST_USER}@notexisting.com</email>
<state>confirmed</state>
</person>
"
${CURL} -X POST "${OBS_URL}/person/${TEST_USER}?cmd=change_password" -d "nots3cr3t"

${CURL} -X PUT "${OBS_URL}/group/testers" -d "<group>
<title>testers</title>
<person>
<person user_id='${TEST_USER}'/>
</person>
</group>"

${CURL} -X PUT "${OBS_URL}/group/admins" -d "<group>
<title>admins</title>
<person>
<person user_id='Admin'/>
</person>
</group>"

${CURL} -X PUT "${OBS_URL}/group/everyone" -d "<group>
<title>everyone</title>
<person>
<person user_id='Admin'/>
<person user_id='${TEST_USER}'/>
</person>
</group>"

# setup interconnect
${CURL} -X PUT "${OBS_URL}/source/openSUSE.org/_meta" -d "<project name='openSUSE.org'>
  <title>Standard OBS instance at build.opensuse.org</title>
  <description>This instance delivers the default build targets for OBS.</description>
  <remoteurl>https://api.opensuse.org/public</remoteurl>
</project>
"

# create openSUSE:Factory first without any repos to avoid the circular
# dependency between Factory and Tumbleweed
${CURL} -X PUT "${OBS_URL}/source/openSUSE:Factory/_meta" -d "
<project name='openSUSE:Factory'>
  <title>The next openSUSE distribution</title>
  <description>Have a look at http://en.opensuse.org/Portal:Factory for more details.</description>
  <repository name='ports'>
    <arch>ppc64le</arch>
    <arch>ppc64</arch>
    <arch>ppc</arch>
    <arch>armv6l</arch>
    <arch>armv7l</arch>
    <arch>aarch64</arch>
  </repository>
</project>
"

${CURL} -X PUT "${OBS_URL}/source/openSUSE:Tumbleweed/_meta" -d "
<project name='openSUSE:Tumbleweed'>
  <title>Tumbleweed</title>
  <description>Tumbleweed is the openSUSE Rolling Release</description>
  <person userid='Admin' role='maintainer'/>
  <build>
    <disable/>
  </build>
  <repository name='standard_debug'>
    <download arch='i586' url='https://download.opensuse.org/debug/tumbleweed/repo/oss' repotype='rpmmd'>
      <archfilter>i686,i586</archfilter>
    </download>
    <download arch='x86_64' url='https://download.opensuse.org/debug/tumbleweed/repo/oss' repotype='rpmmd'>
      <archfilter>x86_64</archfilter>
    </download>
    <arch>i586</arch>
    <arch>x86_64</arch>
  </repository>
  <repository name='standard'>
    <download arch='i586' url='https://download.opensuse.org/tumbleweed/repo/oss' repotype='rpmmd'>
      <archfilter>i686,i586</archfilter>
    </download>
    <download arch='x86_64' url='https://download.opensuse.org/tumbleweed/repo/oss' repotype='rpmmd'>
      <archfilter>x86_64</archfilter>
    </download>
    <download arch='armv6l' url='https://download.opensuse.org/ports/armv6hl/tumbleweed/repo/oss' repotype='rpmmd'>
    </download>
    <download arch='armv7l' url='https://download.opensuse.org/ports/armv7hl/tumbleweed/repo/oss' repotype='rpmmd'>
    </download>
    <download arch='aarch64' url='https://download.opensuse.org/ports/aarch64/tumbleweed/repo/oss' repotype='rpmmd'>
    </download>
    <path project='openSUSE:Tumbleweed' repository='standard_debug'/>
    <path project='openSUSE:Factory' repository='ports'/>
    <arch>i586</arch>
    <arch>x86_64</arch>
    <arch>aarch64</arch>
    <arch>armv7l</arch>
    <arch>armv6l</arch>
  </repository>
</project>
"

${CURL} -X PUT "${OBS_URL}/source/openSUSE:Factory/_meta" -d "
<project name='openSUSE:Factory'>
  <title>The next openSUSE distribution</title>
  <description>Have a look at http://en.opensuse.org/Portal:Factory for more details.</description>
  <person userid='Admin' role='maintainer'/>
  <lock>
    <disable/>
  </lock>
  <build>
    <disable repository='snapshot'/>
    <disable repository='ports'/>
  </build>
  <publish>
    <disable/>
    <enable repository='standard'/>
  </publish>
  <debuginfo>
    <enable/>
  </debuginfo>
  <repository name='standard' rebuild='local'>
    <arch>x86_64</arch>
    <arch>i586</arch>
  </repository>
  <repository name='snapshot'>
    <path project='openSUSE:Tumbleweed' repository='standard'/>
    <arch>x86_64</arch>
    <arch>i586</arch>
  </repository>
  <repository name='ports'>
    <arch>ppc64le</arch>
    <arch>ppc64</arch>
    <arch>ppc</arch>
    <arch>armv6l</arch>
    <arch>armv7l</arch>
    <arch>aarch64</arch>
  </repository>
</project>
"

${CURL} -X PUT "${OBS_URL}/distributions" -d "$(curl https://api.opensuse.org/public/distributions)"

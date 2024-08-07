#
# Copyright 2024 Canonical, Ltd.
# See LICENSE file for licensing details
#

from k8s_test_harness.util import docker_util, env_util


def test_envoy_rock():
    """Test envoy rock."""
    rock = env_util.get_build_meta_info_for_rock_version("envoy", "1.28.2", "amd64")
    image = rock.image

    # check binary and version.
    process = docker_util.run_in_docker(image, ["envoy", "--version"], True)
    assert "envoy" in process.stdout and "1.28.2" in process.stdout

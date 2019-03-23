# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.13.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class V1JobSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'active_deadline_seconds': 'int',
        'backoff_limit': 'int',
        'completions': 'int',
        'manual_selector': 'bool',
        'parallelism': 'int',
        'selector': 'V1LabelSelector',
        'template': 'V1PodTemplateSpec',
        'ttl_seconds_after_finished': 'int'
    }

    attribute_map = {
        'active_deadline_seconds': 'activeDeadlineSeconds',
        'backoff_limit': 'backoffLimit',
        'completions': 'completions',
        'manual_selector': 'manualSelector',
        'parallelism': 'parallelism',
        'selector': 'selector',
        'template': 'template',
        'ttl_seconds_after_finished': 'ttlSecondsAfterFinished'
    }

    def __init__(self, active_deadline_seconds=None, backoff_limit=None, completions=None, manual_selector=None, parallelism=None, selector=None, template=None, ttl_seconds_after_finished=None):  # noqa: E501
        """V1JobSpec - a model defined in OpenAPI"""  # noqa: E501

        self._active_deadline_seconds = None
        self._backoff_limit = None
        self._completions = None
        self._manual_selector = None
        self._parallelism = None
        self._selector = None
        self._template = None
        self._ttl_seconds_after_finished = None
        self.discriminator = None

        if active_deadline_seconds is not None:
            self.active_deadline_seconds = active_deadline_seconds
        if backoff_limit is not None:
            self.backoff_limit = backoff_limit
        if completions is not None:
            self.completions = completions
        if manual_selector is not None:
            self.manual_selector = manual_selector
        if parallelism is not None:
            self.parallelism = parallelism
        if selector is not None:
            self.selector = selector
        self.template = template
        if ttl_seconds_after_finished is not None:
            self.ttl_seconds_after_finished = ttl_seconds_after_finished

    @property
    def active_deadline_seconds(self):
        """Gets the active_deadline_seconds of this V1JobSpec.  # noqa: E501

        Specifies the duration in seconds relative to the startTime that the job may be active before the system tries to terminate it; value must be positive integer  # noqa: E501

        :return: The active_deadline_seconds of this V1JobSpec.  # noqa: E501
        :rtype: int
        """
        return self._active_deadline_seconds

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds):
        """Sets the active_deadline_seconds of this V1JobSpec.

        Specifies the duration in seconds relative to the startTime that the job may be active before the system tries to terminate it; value must be positive integer  # noqa: E501

        :param active_deadline_seconds: The active_deadline_seconds of this V1JobSpec.  # noqa: E501
        :type: int
        """

        self._active_deadline_seconds = active_deadline_seconds

    @property
    def backoff_limit(self):
        """Gets the backoff_limit of this V1JobSpec.  # noqa: E501

        Specifies the number of retries before marking this job failed. Defaults to 6  # noqa: E501

        :return: The backoff_limit of this V1JobSpec.  # noqa: E501
        :rtype: int
        """
        return self._backoff_limit

    @backoff_limit.setter
    def backoff_limit(self, backoff_limit):
        """Sets the backoff_limit of this V1JobSpec.

        Specifies the number of retries before marking this job failed. Defaults to 6  # noqa: E501

        :param backoff_limit: The backoff_limit of this V1JobSpec.  # noqa: E501
        :type: int
        """

        self._backoff_limit = backoff_limit

    @property
    def completions(self):
        """Gets the completions of this V1JobSpec.  # noqa: E501

        Specifies the desired number of successfully finished pods the job should be run with.  Setting to nil means that the success of any pod signals the success of all pods, and allows parallelism to have any positive value.  Setting to 1 means that parallelism is limited to 1 and the success of that pod signals the success of the job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :return: The completions of this V1JobSpec.  # noqa: E501
        :rtype: int
        """
        return self._completions

    @completions.setter
    def completions(self, completions):
        """Sets the completions of this V1JobSpec.

        Specifies the desired number of successfully finished pods the job should be run with.  Setting to nil means that the success of any pod signals the success of all pods, and allows parallelism to have any positive value.  Setting to 1 means that parallelism is limited to 1 and the success of that pod signals the success of the job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :param completions: The completions of this V1JobSpec.  # noqa: E501
        :type: int
        """

        self._completions = completions

    @property
    def manual_selector(self):
        """Gets the manual_selector of this V1JobSpec.  # noqa: E501

        manualSelector controls generation of pod labels and pod selectors. Leave `manualSelector` unset unless you are certain what you are doing. When false or unset, the system pick labels unique to this job and appends those labels to the pod template.  When true, the user is responsible for picking unique labels and specifying the selector.  Failure to pick a unique label may cause this and other jobs to not function correctly.  However, You may see `manualSelector=true` in jobs that were created with the old `extensions/v1beta1` API. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#specifying-your-own-pod-selector  # noqa: E501

        :return: The manual_selector of this V1JobSpec.  # noqa: E501
        :rtype: bool
        """
        return self._manual_selector

    @manual_selector.setter
    def manual_selector(self, manual_selector):
        """Sets the manual_selector of this V1JobSpec.

        manualSelector controls generation of pod labels and pod selectors. Leave `manualSelector` unset unless you are certain what you are doing. When false or unset, the system pick labels unique to this job and appends those labels to the pod template.  When true, the user is responsible for picking unique labels and specifying the selector.  Failure to pick a unique label may cause this and other jobs to not function correctly.  However, You may see `manualSelector=true` in jobs that were created with the old `extensions/v1beta1` API. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#specifying-your-own-pod-selector  # noqa: E501

        :param manual_selector: The manual_selector of this V1JobSpec.  # noqa: E501
        :type: bool
        """

        self._manual_selector = manual_selector

    @property
    def parallelism(self):
        """Gets the parallelism of this V1JobSpec.  # noqa: E501

        Specifies the maximum desired number of pods the job should run at any given time. The actual number of pods running in steady state will be less than this number when ((.spec.completions - .status.successful) < .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :return: The parallelism of this V1JobSpec.  # noqa: E501
        :rtype: int
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """Sets the parallelism of this V1JobSpec.

        Specifies the maximum desired number of pods the job should run at any given time. The actual number of pods running in steady state will be less than this number when ((.spec.completions - .status.successful) < .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :param parallelism: The parallelism of this V1JobSpec.  # noqa: E501
        :type: int
        """

        self._parallelism = parallelism

    @property
    def selector(self):
        """Gets the selector of this V1JobSpec.  # noqa: E501


        :return: The selector of this V1JobSpec.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this V1JobSpec.


        :param selector: The selector of this V1JobSpec.  # noqa: E501
        :type: V1LabelSelector
        """

        self._selector = selector

    @property
    def template(self):
        """Gets the template of this V1JobSpec.  # noqa: E501


        :return: The template of this V1JobSpec.  # noqa: E501
        :rtype: V1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this V1JobSpec.


        :param template: The template of this V1JobSpec.  # noqa: E501
        :type: V1PodTemplateSpec
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

    @property
    def ttl_seconds_after_finished(self):
        """Gets the ttl_seconds_after_finished of this V1JobSpec.  # noqa: E501

        ttlSecondsAfterFinished limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, ttlSecondsAfterFinished after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is unset, the Job won't be automatically deleted. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes. This field is alpha-level and is only honored by servers that enable the TTLAfterFinished feature.  # noqa: E501

        :return: The ttl_seconds_after_finished of this V1JobSpec.  # noqa: E501
        :rtype: int
        """
        return self._ttl_seconds_after_finished

    @ttl_seconds_after_finished.setter
    def ttl_seconds_after_finished(self, ttl_seconds_after_finished):
        """Sets the ttl_seconds_after_finished of this V1JobSpec.

        ttlSecondsAfterFinished limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, ttlSecondsAfterFinished after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is unset, the Job won't be automatically deleted. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes. This field is alpha-level and is only honored by servers that enable the TTLAfterFinished feature.  # noqa: E501

        :param ttl_seconds_after_finished: The ttl_seconds_after_finished of this V1JobSpec.  # noqa: E501
        :type: int
        """

        self._ttl_seconds_after_finished = ttl_seconds_after_finished

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1JobSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
